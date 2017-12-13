import boto3
from botocore.client import Config
import StringIO
import zipfile

def lambda_handler(event, context):
	sns = boto3.resource('sns')
	topic = sns.Topic('arn:aws:sns:us-east-1:384512602151:deployPortfolioTopic')
	try:
	    s3 = boto3.resource('s3', config=Config(signature_version-'s3v4'))

	    portfolio_bucket = s3.Bucket('portfolio.despenny.rocks')
	    build_bucket = s3.Bucket('portfoliobuild.despenny.rocks')
	    
	    portfolio_zip = StringIO.StringIO()
	    build_bucket.download_fileobj('portfoliobuild.zip', portfolio_zip)

		with zipfile.ZipFile(portfolio_zip) as myzip:
			for nm in myzip.namelist():
				obj = myzip.open(nm)
				portfolio_bucket.upload_fileonj(obj, nm, ExtraArgs={'ContentType':mimetypes_guesstype(nm)[0]})
				portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
		print "Deployed!"

		topic.publish(Subject="Portfolio deployed", Message="Portfolio Deployed Successfully!")
	except:
    	topic.publish(Subject="Portfolio deploy Failed", Message="Portfolio failed to deploy!")
    	raise
    return "Hello from Lambda"