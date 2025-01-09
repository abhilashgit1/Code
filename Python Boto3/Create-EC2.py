import boto3
import boto3.session

aws_management_console = boto3.session.Session(profile_name="default")
ec2_console=aws_management_console.client('ec2')
response=ec2_console.run_instances(
    ImageId='ami-0453ec754f44f9a4a',
    InstanceType='t2.micro',
    Mincount=1,
    Maxcount=1
)