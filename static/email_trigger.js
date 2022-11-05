// Function to send email notification when the sign-up form is submitted
function submitToAPI(e) {
    e.preventDefault();
    var API_URL = "https://hroi05yadf.execute-api.us-east-1.amazonaws.com/emailstage";

    // Retrieve the email address and passwords from your form here.  As an example, in our sign up form we're
    // using the HTML "name" element to refer to the email, password, and password-confirm fields in the form
    var email = $('input[name="email"]').val();
    var password = $('input[name="password"]').val();
    var confirm_password =$('input[name="confirm_password"]').val();

    // Perform any form validation you'd like in this section.  What should happen if a user provides an email without a domain?
    // (e.g. abc123 instead of abc123@example.com).  What if the provided passwords don't match?  Should there be any restrictions
    // around passwords to provide more security for the customer?
   
    // Set the data to pass to the API.  Feel free to change this section as needed
    var data = {
        email: email,
        password: password,
        confirm_password: confirm_password
    };
    
    // Utilze Ajax to send an HTTPS POST request to your API
    $.ajax({
        type: "POST",
        url: API_URL,
        dataType: "json",
        crossDomain: true,
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data),
        success: function() {
            // Can you think of anything you'd want to do to notify a customer that they've been sent a welcome email?
        
            // Clear the form data after submission
            $('#signup-form')[0].reset();
        },
        error: function() {
            // Can you think of anything you'd want to do to notify the customer that we (Amazon) failed to send them a welcome email?
            
            // Clear the form data after submission
            $('#signup-form')[0].reset();
        }
    });
} 
