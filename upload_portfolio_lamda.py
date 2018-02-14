import boto3
from botocore.client import Config
import StringIO
import mimetypes
import zipfile

def lambda_handler(event, context):
	sns = boto3.resource('sns')
	topic = sns.Topic('arn:aws:sns:us-east-1:384512602151:deployPortfolioTopic')

	location = {
		"bucketName": 'portfoliobuild.despenny.rocks',
		"objectKey": 'portfoliobuild.zip'
	}
	try:
		job = event.get("CodePipeline.job")

		if job:
			for artifact in  job["data"]["inputArtifacts"]:
				if artifact["name"] == "MyAppBuild":
					location = artifact["location"]["s3Location"]

		print "Building Portfolio from "+ str(location)

		s3 = boto3.resource('s3', config=Config(signature_version='s3v4'))

		portfolio_bucket = s3.Bucket('portfolio.despenny.rocks')
		build_bucket = s3.Bucket(location["bucketName"])

		portfolio_zip = StringIO.StringIO()
		build_bucket.download_fileobj(location["objectKey"], portfolio_zip)

		with zipfile.ZipFile(portfolio_zip) as myzip:
			for nm in myzip.namelist():
				obj = myzip.open(nm)
				portfolio_bucket.upload_fileobj(obj, nm, ExtraArgs={'ContentType': mimetypes.guess_type(nm)[0]})
				portfolio_bucket.Object(nm).Acl().put(ACL='public-read')
		print "Deployed!"

		topic.publish(Subject="Portfolio deployed", Message="Portfolio Deployed Successfully!")
		if job:
			codepipeline = boto3.client('codepipeline')
			codepipeline.put_job_success_result(jobId=job["id"])
	except:
		topic.publish(Subject="Portfolio deploy Failed", Message="Portfolio failed to deploy!")
		raise
	return "Hello from Lambda"
