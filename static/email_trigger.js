// Function to send email notification when the sign-up form is submitted
function submitToAPI(e) {
    e.preventDefault();
    var API_URL = "https://hroi05yadf.execute-api.us-east-1.amazonaws.com/Beta/emailtrigger";

    // Retrieve the email address and passwords from your form here.  As an example, in our sign up form we're
    // using the HTML "name" element to refer to the email, password, and password-confirm fields in the form
    var email = $('input[name="email"]').val();
    var password = $('input[name="password"]').val();
    var confirm_password =$('input[name="confirm_password"]').val();
    
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
            
            //$('#signup-form')[0].reset();
        },
        error: function() {
           
            //$('#signup-form')[0].reset();
        }
    });
} 
