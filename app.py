import streamlit as st

st.title("Panopto Permissions Troubleshooter")
st.write("Having trouble with Panopto video access? I’ll guide you through a few quick checks.")

# Step 1: How are students accessing the video?
step1 = st.radio("How are students accessing the video?", [
    "Embedded in Canvas",
    "Direct link or email",
    "Panopto directly"
])

if step1 == "Embedded in Canvas":
    step2 = st.radio("How is the video embedded?", [
        "Panopto LTI Embed",
        "iFrame embed"
    ])

    if step2 == "Panopto LTI Embed":
        st.success("✅ This method usually inherits course permissions automatically. Make sure the video is stored in the Canvas course folder.")
    else:
        st.warning("⚠️ iFrame embeds do not carry course permissions. Re-embed using the Panopto LTI tool in Canvas.")

elif step1 == "Direct link or email":
    step3 = st.radio("Is the video shared with 'Anyone at your institution with the link'?", [
        "Yes",
        "No",
        "I’m not sure"
    ])

    if step3 == "Yes":
        st.success("✅ Anyone with the link can view it—this should work unless the viewer is outside your institution.")
    else:
        st.warning("⚠️ You need to either share it with the course or update the sharing settings to include the right audience.")

elif step1 == "Panopto directly":
    step4 = st.radio("Is the video located in the Canvas course folder?", [
        "Yes",
        "No",
        "I’m not sure"
    ])

    if step4 == "Yes":
        st.success("✅ Students enrolled in the course should have access automatically. If not, double-check group permissions on the folder.")
    else:
        st.warning("⚠️ Move the video into the appropriate Canvas course folder so permissions match enrolled students.")

st.write("\n---\n")
st.info("Need more help? Contact your campus support team or visit the Panopto support center.")
