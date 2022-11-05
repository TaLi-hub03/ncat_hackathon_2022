import json
import boto3
from botocore.exceptions import ClientError

# Replace the sender@example.com with the "From" address emails should come from.  Must be verified by AWS SES
SENDER = "fdgarciacruz@aggies.ncat.edu"

# Replace the AWS_REGION with the region you've deployed SES to
AWS_REGION = "us-east-1"

# Character encoding for the email
CHARSET = 'UTF-8'

def lambda_handler(event, context):
    print("Received event object: {}".format(event))
    
    # Retrieve the email from the signup form and send a notification via SES
    try:
        # Check and ensure that an "email" address was passed in to this function
        if 'email' not in event:
            raise KeyError("No email provided in event object, aborting...")
        email = event['email']
        
        # Create a "subject" variable which will be the subject line of the welcome email
        subject = "Welcome to Amazon Prime Student!"
        
        # Create the HTML string that will populate the "body" of the email
        body_html = """
            <html>
                <head></head>
                <body>
                    Welcome to your Amazon Prime Student account. There are multiple plans and packages that are at your needs and wants as a college student.
                    You have access to Amazon closet to choose clothes that best suites any occassion wherever you are studying, Amazon Hygiene to best maintain
                    your physical and mental health in balance, Amazon College Essentials to be able to purchase the best materials you will need for class or studying,
                    and Amazon Late Nights to be stocked on snacks and meals to help avoid going days without eating. You will have access to many
                    Amazon platform shows and deals that are in the best interest for your finances and help ensure your Amazon Prime Student account
                    serves you at the best it can be. We hope you enjoy your plan and let us know if there are any changes that can
                    better service your needs. Please enjoy.
                    
                    Thank You,
                    The Amazon Prime Team
                </body>
            </html>
        """

        # Backup string in case the email client doesn't support HTML for emails (unlikely)
        body_text = """
            Welcome to your Amazon Prime Student account.
            There are multiple plans and packages that are at your needs and wants as a college student.
            Please enjoy.
        """

        # Send the email using the send_email() function and note the response
        response = send_email(subject=subject, email_body_html=body_html, email_body_text=body_text, recipient=email)
        
        # If we get here, we can return a "success" response of HTTP.status_code = 200
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "isBase64Encoded": False,
            "body": json.dumps({
                "result": "Email send success!",
                "messageId": response['MessageId'],
                'requestId': context.aws_request_id
            })
        }
    except KeyError as e:
        raise Exception("No data field present in event object")
    except ClientError as e:
        print(e.response['Error']['Message'])
        raise Exception("Failed to send the notification email to {}".format(email))

# Function to send the welcome email
def send_email(subject, email_body_html, email_body_text, recipient):
    client = boto3.client('ses', region_name=AWS_REGION)
    response = client.send_email(
        Destination = {
            'ToAddresses': [
                recipient,    
            ],
        },
        Message= {
            'Body': {
                'Html': {
                    'Charset': CHARSET,
                    'Data': email_body_html,
                },
                'Text': {
                    'Charset': CHARSET,
                    'Data': (email_body_text),
                },
            },
            'Subject': {
                'Charset': CHARSET,
                'Data': subject,
            },
        },
        Source=SENDER
    )
    return response
