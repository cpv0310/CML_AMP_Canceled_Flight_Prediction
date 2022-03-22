# ###########################################################################
#
#  CLOUDERA APPLIED MACHINE LEARNING PROTOTYPE (AMP)
#  (C) Cloudera, Inc. 2021
#  All rights reserved.
#
#  Applicable Open Source License: Apache 2.0
#
#  NOTE: Cloudera open source products are modular software products
#  made up of hundreds of individual components, each of which was
#  individually copyrighted.  Each Cloudera open source product is a
#  collective work under U.S. Copyright Law. Your license to use the
#  collective work is as provided in your written agreement with
#  Cloudera.  Used apart from the collective work, this file is
#  licensed for your use pursuant to the open source license
#  identified above.
#
#  This code is provided to you pursuant a written agreement with
#  (i) Cloudera, Inc. or (ii) a third-party authorized to distribute
#  this code. If you do not have a written agreement with Cloudera nor
#  with an authorized and properly licensed third party, you do not
#  have any rights to access nor to use this code.
#
#  Absent a written agreement with Cloudera, Inc. (“Cloudera”) to the
#  contrary, A) CLOUDERA PROVIDES THIS CODE TO YOU WITHOUT WARRANTIES OF ANY
#  KIND; (B) CLOUDERA DISCLAIMS ANY AND ALL EXPRESS AND IMPLIED
#  WARRANTIES WITH RESPECT TO THIS CODE, INCLUDING BUT NOT LIMITED TO
#  IMPLIED WARRANTIES OF TITLE, NON-INFRINGEMENT, MERCHANTABILITY AND
#  FITNESS FOR A PARTICULAR PURPOSE; (C) CLOUDERA IS NOT LIABLE TO YOU,
#  AND WILL NOT DEFEND, INDEMNIFY, NOR HOLD YOU HARMLESS FOR ANY CLAIMS
#  ARISING FROM OR RELATED TO THE CODE; AND (D)WITH RESPECT TO YOUR EXERCISE
#  OF ANY RIGHTS GRANTED TO YOU FOR THE CODE, CLOUDERA IS NOT LIABLE FOR ANY
#  DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, PUNITIVE OR
#  CONSEQUENTIAL DAMAGES INCLUDING, BUT NOT LIMITED TO, DAMAGES
#  RELATED TO LOST REVENUE, LOST PROFITS, LOSS OF INCOME, LOSS OF
#  BUSINESS ADVANTAGE OR UNAVAILABILITY, OR LOSS OR CORRUPTION OF
#  DATA.
#
# ###########################################################################

# Install the requirements
!pip install --progress-bar off -r requirements.txt
!pip install https://$CDSW_DOMAIN/api/v2/python.tar.gz


import cmlapi
import os
import json


def set_environ(Cml,Item,Value):
  Project=Cml.get_project(os.getenv("CDSW_PROJECT_ID"))
  if Project.environment=='':
    Project_Environment={}
  else:
    Project_Environment=json.loads(Project.environment)
  Project_Environment[Item]=Value
  Project.environment=json.dumps(Project_Environment)
  Cml.update_project(Project,project_id=os.getenv("CDSW_PROJECT_ID"))

def get_environ(Cml,Item):
  Project=Cml.get_project(os.getenv("CDSW_PROJECT_ID"))
  Project_Environment=json.loads(Project.environment)
  return Project_Environment[Item]

# Set the setup variables needed by CML APIv2
HOST = os.getenv("CDSW_API_URL").split(":")[0] + "://" + os.getenv("CDSW_DOMAIN")
USERNAME = os.getenv("CDSW_PROJECT_URL").split("/")[6]  # args.username  # "vdibia"
API_KEY = os.getenv("CDSW_APIV2_KEY")
PROJECT_NAME = os.getenv("CDSW_PROJECT")
PROJECT_ID=os.getenv("CDSW_PROJECT_ID")

# Instantiate API Wrapper
cml = cmlapi.default_client(url=HOST,cml_api_key=API_KEY)


#set Project environment variables
set_environ(cml,"HIVE_DATABASE","airline")
set_environ(cml,"HIVE_TABLE","flights")
set_environ(cml,"STORAGE_PATH",os.environ["STORAGE"]+os.environ["HOME"]+"/"+PROJECT_NAME)

project=cml.get_project(PROJECT_ID)
print("Project Environment Variables :"+ project.environment)
