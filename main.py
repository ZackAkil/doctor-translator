import streamlit as st

example_report="There is a complete rupture of the ACL at its midsubstance with anterior tibial translation. There is bone marrow oedema at the sulcus terminalis of the lateral femoral condyle as well as the posterolateral corner of the lateral tibial plateau. There is further bone marrow oedema with a small fracture through the subchondral bone plate at the posteromedial corner of the medial tibial plateau. The PCL is intact."

st.set_page_config(
    page_title="Medical Report Translator",
    page_icon="🏥")


if 'translated_report' not in st.session_state:
    st.session_state.translated_report = ''
if 'approved' not in st.session_state:
    st.session_state.approved = False
    

st.header(' 🏥 Medical Report Translator', divider='red')
st.caption('Raw medical reports with all their big words can be scary to read as the patient. Using Gemini we can generate a report so that it\'s more readable by the patient (assuming they are not medical experts).')


def translate_report(text):
    from gemini import translate_doctor_report
    return translate_doctor_report(text)


report = st.text_area(
"Raw medical report:",
example_report, height=200
)


if st.button('Translate', disabled= not report):
    st.session_state.translated_report = None
    with st.spinner('Generating report...'):
        st.session_state.translated_report = translate_report(report)



if st.session_state.translated_report:

    st.subheader('Patient friendly report')

    with st.container(border=True):
        st.markdown(
        st.session_state.translated_report
        )

    report_accurate = st.checkbox('As a qualified professional I confirm that the translated report is accurate.', 
                                  value=False, 
                                  help='This is our way of ensuring our app is IVO compliant.')


    if st.button('Send report to patient' ,disabled=(not report_accurate)):
        st.success('Report sent to patient.', icon='✅')
