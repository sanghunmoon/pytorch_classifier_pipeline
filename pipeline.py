# pipeline.py

from kfp import dsl
@dsl.pipeline(
    name='pytorch_classifier_test_2',
    description='basic python classifier',
)

# n_num을 함수의 매개변수로 지정
def mlflow_pipeline():
  ml = dsl.ContainerOp(
      name="training pipeline",
      image="lego0142/pytorch_classifier:1.1",
  )
    
if __name__ == "__main__":

    import kfp.compiler as compiler

		# Pipeline 파일 생성
    compiler.Compiler().compile(mlflow_pipeline, "sh_pytorch_classifier.tar.gz")