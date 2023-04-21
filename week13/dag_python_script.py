from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import KubernetesPodOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from datetime import datetime
from kubernetes.client import models as k8s

volume = k8s.V1Volume(
    name='test-volume',
    persistent_volume_claim=k8s.V1PersistentVolumeClaimVolumeSource(claim_name='centos-pv-claim'),
)

volume_mount = k8s.V1VolumeMount(
    name='test-volume', mount_path='/root/mount_file', sub_path=None
)

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
}

dag = DAG(
    'run_python_script',
    default_args=default_args,
    schedule_interval='@once'
)

# load data from mysql and create a csv file
task1 = KubernetesPodOperator(
            namespace='airflow',
            name="task1",
            task_id="task1",
            image="dlambrig/python-uml:latest",
            cmds=["bash","-c"],
            arguments=["/run.sh"],
            labels={"foo": "bar"},
            volumes=[volume],
            volume_mounts=[volume_mount],
            get_logs=True,
            dag=dag
                              )

# upload to s3
task2 = KubernetesPodOperator(
            task_id='task2',
            name='task2',
            namespace='airflow',
            volumes=[volume],
            volume_mounts=[volume_mount],
            env_vars={
                'PYTHONPATH': '/root/mount_file',
                'AIRFLOW_CONN_AWS': '{{ var.value.aws_conn }}',
                'AWS_ACCESS': '{{ var.value.AWSA }}',
                'AWS_SECRET': '{{ var.value.AWSB }}'
            },
            image='dlambrig/week13:1.0',
            cmds=['python', '-c', 'from my_function import my_function; my_function()'],
            arguments=[],
            dag=dag,
)

task1 >> task2
