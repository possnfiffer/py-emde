ndata = []
with open('data/windspd_20160202.dat') as f:
    for line in f:
        ndata.append(line.split(" "))

flist = []
for l in ndata:
    if l[4].endswith('00') or l[4].endswith('15') or l[4].endswith('30') or l[4].endswith('45'):
        flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + l[6]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')

fstring = ''
for l in flist:
    fstring += l + ' '

data = '//AA ' + fstring + '//ZZ'


from sparkpost import SparkPost


# Send email using the SparkPost api
sp = SparkPost() # uses environment variable named SPARKPOST_API_KEY

response = sp.transmission.send(
        recipients=['practicedata@globe.gov'],
        bcc=['aroller@ucar.edu'],
        text=data,
        from_email='roller@rollercomsolutions.com',
        subject='DATA'
)

print(response)
