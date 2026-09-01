"""
Admin panel: lets SFT upload a new assumptions.xlsx
"""

import base64
import requests
import streamlit as st

GITHUB_API_URL = "https://api.github.com"


def _github_headers():
    token = st.secrets["github"]["token"]
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }


def _get_existing_file_sha(owner, repo, path, branch):
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/contents/{path}"
    resp = requests.get(url, headers=_github_headers(), params={"ref": branch})
    if resp.status_code == 200:
        return resp.json()["sha"]
    return None


def commit_assumptions_file(file_bytes: bytes, commit_message: str) -> tuple[bool, str]:
    """Commits the uploaded file to the configured GitHub repo path.
    Returns (success, message)."""
    cfg = st.secrets["github"]
    owner = cfg["owner"]
    repo = cfg["repo"]
    path = cfg["assumptions_path"]
    branch = cfg.get("branch", "main")

    sha = _get_existing_file_sha(owner, repo, path, branch)

    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/contents/{path}"
    payload = {
        "message": commit_message,
        "content": base64.b64encode(file_bytes).decode(),
        "branch": branch,
    }
    if sha:
        payload["sha"] = sha

    resp = requests.put(url, headers=_github_headers(), json=payload)

    if resp.status_code in (200, 201):
        return True, "Assumptions file updated successfully."
    return False, f"GitHub API error ({resp.status_code}): {resp.json().get('message', resp.text)}"


def render_admin_panel(clear_assumptions_cache):
    """Renders the password-gated admin panel in the sidebar.
    clear_assumptions_cache is get_assumptions.clear, called after a successful
    upload so the app picks up the new file immediately."""
    with st.sidebar.expander("Admin", expanded=False):
        password = st.text_input("Admin password", type="password", key="admin_pw")
        if password != st.secrets.get("admin_password", None):
            if password:
                st.error("Incorrect password.")
            return

        st.success("Admin access granted.")

        # Show the result of the last upload, if there was one
        if "admin_last_result" in st.session_state:
            success, message = st.session_state.pop("admin_last_result")
            if success:
                st.success(message)
            else:
                st.error(message)

        st.caption("Upload a new assumptions.xlsx to replace the current version. "
                   "This is committed to GitHub and takes effect immediately.")

        uploaded = st.file_uploader("New assumptions.xlsx", type=["xlsx"], key="admin_upload")
        if uploaded is not None:
            if st.button("Publish this update", type="primary"):
                with st.spinner("Uploading to GitHub..."):
                    success, message = commit_assumptions_file(
                        uploaded.getvalue(),
                        commit_message="Update assumptions.xlsx via admin panel",
                    )
                st.session_state["admin_last_result"] = (success, message)
                if success:
                    clear_assumptions_cache()
                st.rerun()