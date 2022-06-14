#!/usr/bin/env python3
import os

import aws_cdk as cdk

from mlinfra.init_stack import InitStack

region = "eu-west-1"
account = "691513757250"
env = cdk.Environment(account=account, region=region)

app = cdk.App()

init = InitStack(app, "ml-init", env=env)


app.synth()
