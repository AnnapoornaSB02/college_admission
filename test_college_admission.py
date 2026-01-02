from college_admission import apply_admission, view_application

def test_application_submission():
    result = apply_admission("A101", "Anu", "CSE", 85)
    assert result == "Application submitted successfully"

def test_duplicate_application():
    apply_admission("A102", "Ravi", "ECE", 70)
    result = apply_admission("A102", "Ravi", "ECE", 70)
    assert result == "Application already exists"

def test_application_status():
    apply_admission("A103", "Meena", "IT", 55)
    status = view_application("A103")
    assert status["status"] == "Rejected"