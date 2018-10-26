
# coding: utf-8

# In[117]:


import requests
from google.cloud import storage
import os


# In[131]:


def get_file_from_gcs(file_name, bucket_name='sap_gcp_mm_si_uplds_batch'):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.get_blob(file_name)
    blob.download_to_filename(file_name)
    f = open(file_name, 'rb')
    return f


# In[132]:


def call_ml_ocr_with_binary(f_binary, file_name):
    url = 'http://sap-dev-sbox.appspot.com/api2'
    files = {'file': f_binary}
    res = requests.post(url, files=files)
    print(res.text)


# In[133]:


def call_ocr_from_pubsub(file_name):
    b = get_file_from_gcs(file_name)
    a = call_ml_ocr_with_binary(b, file_name)


# In[ ]:


def file_upload_pubsub_handle(data, context):
    print('Event ID: {}'.format(context.event_id))
    print('Event type: {}'.format(context.event_type))
    print('Bucket: {}'.format(data['bucket']))
    print('File: {}'.format(data['name']))
    print('Metageneration: {}'.format(data['metageneration']))
    print('Created: {}'.format(data['timeCreated']))
    print('Updated: {}'.format(data['updated']))


# In[134]:


#call_ocr_from_pubsub('image.jpg')

