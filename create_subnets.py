import boto3

response = client.create_vpc(
    CidrBlock='string',
    AmazonProvidedIpv6CidrBlock=True|False,
    Ipv6Pool='string',
    Ipv6CidrBlock='string',
    DryRun=True|False,
    InstanceTenancy='default'|'dedicated'|'host',
    Ipv6CidrBlockNetworkBorderGroup='string'
)