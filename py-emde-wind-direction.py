ndata = []
with open('data/winddir_20160202.dat') as f:
    for line in f:
        ndata.append(line.split(" "))

flist = []
for l in ndata:
    if l[4].endswith('00') or l[4].endswith('15') or l[4].endswith('30') or l[4].endswith('45'):
        if float(l[-1].strip()) == 0 or float(l[-1].strip()) == 360:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'N'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
# NNE = 22.5º
        elif float(l[-1].strip()) > 0 and float(l[-1].strip()) <= 22.5:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'NNE'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#NE = 45º
        elif float(l[-1].strip()) > 22.5 and float(l[-1].strip()) <= 45:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'NE'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#ENE = 67.5º
        elif float(l[-1].strip()) > 45 and float(l[-1].strip()) <= 67.5:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'ENE'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#E = 90º
        elif float(l[-1].strip()) > 67.5 and float(l[-1].strip()) <= 90:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'E'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#ESE = 112.5º
        elif float(l[-1].strip()) > 90 and float(l[-1].strip()) <= 112.5:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'ESE'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#SE = 135º
        elif float(l[-1].strip()) > 112.5 and float(l[-1].strip()) <= 135:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'SE'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#SSE = 157.5º
        elif float(l[-1].strip()) > 135 and float(l[-1].strip()) <= 157.5:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'SSE'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#S = 180º
        elif float(l[-1].strip()) > 157.5 and float(l[-1].strip()) <= 180:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'S'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#SSW = 202.5º
        elif float(l[-1].strip()) > 180 and float(l[-1].strip()) <= 202.5:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'SSW'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#SW = 225º
        elif float(l[-1].strip()) > 202.5 and float(l[-1].strip()) <= 225:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'SW'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#WSW = 247.5º
        elif float(l[-1].strip()) > 225 and float(l[-1].strip()) <= 247.5:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'WSW'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#W = 270º
        elif float(l[-1].strip()) > 247.5 and float(l[-1].strip()) <= 270:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'W'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#WNW = 292.5º
        elif float(l[-1].strip()) > 270 and float(l[-1].strip()) <= 292.5:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'WNW'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#NW = 315º
        elif float(l[-1].strip()) > 292.5 and float(l[-1].strip()) <= 315:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'NW'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')
#NNW = 337.5º
        elif float(l[-1].strip()) > 315 and float(l[-1].strip()) <= 337.5:
            flist.append('DAVAD ZZCOUCAR SITE_ID:32534' + ' ' + l[2]+ l[0]+ l[1]+ l[3]+ l[4]+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'NNW'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X'+ ' ' + 'X')

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
