def determine_loan_approval(credit_score, annual_income):
    
    if credit_score >= 750 and annual_income >= 50000:
        return "Approved"
    
    elif 650 <= credit_score < 750 and annual_income >= 30000:
        return "Approved"
    
    elif 550 <= credit_score < 650 and annual_income < 30000:
        return "Review"
    else:
        return "Not Approved"

        
    