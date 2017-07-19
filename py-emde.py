from sparkpost import SparkPost


# Send email using the SparkPost api
sp = SparkPost() # uses environment variable named SPARKPOST_API_KEY

response = sp.transmission.send(
        recipients=['practicedata@globe.gov'],
        bcc=['aroller@ucar.edu'],
        text='//AA DAVAD ZZCOUCAR SITE_ID:32534 201707190100 28 M M M M X X X X X //ZZ',
        from_email='roller@rollercomsolutions.com',
        subject='DATA'
)

print(response)


# Send email using SMTP
