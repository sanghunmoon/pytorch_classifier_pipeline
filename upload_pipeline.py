import requests
import kfp

KubeflowServer = ""
client = kfp.Client(KubeflowServer)

# pipeline 생성
pipeline = client.upload_pipeline(pipeline_package_path='sh_pytorch_classifier.tar.gz',
pipeline_name='pytorch_classifier_test_2')


# experiment 생성 및 실행
experiment = client.create_experiment(name="", namespace="")
result = client.run_pipeline(
    experiment_id=experiment.id,
    #job_name=model_nm,
    pipeline_id=pipeline.id,
    #params=params,
)


print("kubeflow result : ", result)
print("kubeflow run_id : ", result.id)
