from vertexai.preview.generative_models import GenerativeModel

# Load Gemini Pro
gemini_pro_model = GenerativeModel("gemini-pro")


def translate_doctor_report(report):
    prompt = f'''Summaries the following doctor report so that its more easily understood by the patient: {report} ... 
    Summary Report: 
    '''
    return call_gemini(prompt)


def call_gemini(prompt):
    model_response = gemini_pro_model.generate_content(prompt)
    return model_response.text