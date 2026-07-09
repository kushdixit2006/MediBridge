import requests
import streamlit as st

BACKEND_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="MediBridge",
    page_icon="🩺",
    layout="wide",
)

st.title("🩺 MediBridge")
st.write("Upload a medical report and ask questions about it.")

if "session_id" not in st.session_state:
    st.session_state.session_id = None

if "messages" not in st.session_state:
    st.session_state.messages = []

uploaded_file = st.file_uploader(
    "Upload Medical Report",
    type=["pdf"],
)

if uploaded_file is not None and st.session_state.session_id is None:

    with st.spinner("Processing report..."):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf",
            )
        }

        try:

            response = requests.post(
                f"{BACKEND_URL}/api/upload",
                files=files,
                timeout=120,
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state.session_id = data["session_id"]

                st.success(data["message"])

            else:

                try:
                    st.error(response.json()["detail"])
                except Exception:
                    st.error(response.text)

        except requests.exceptions.RequestException as e:
            st.error(f"Backend connection failed:\n{e}")

if st.session_state.session_id:

    st.divider()

    st.subheader("Chat with MediBridge")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    prompt = st.chat_input(
        "Ask something about your report..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Thinking..."):

            try:

                response = requests.post(
                    f"{BACKEND_URL}/api/chat",
                    json={
                        "session_id": st.session_state.session_id,
                        "question": prompt,
                    },
                    timeout=120,
                )

                if response.status_code == 200:

                    answer = response.json()["answer"]

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer,
                        }
                    )

                    with st.chat_message("assistant"):
                        st.markdown(answer)

                else:

                    try:
                        st.error(response.json()["detail"])
                    except Exception:
                        st.error(response.text)

            except requests.exceptions.RequestException as e:
                st.error(f"Backend connection failed:\n{e}")