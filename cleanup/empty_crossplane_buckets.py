import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def empty_bucket(bucket_name):
    s3_resource = boto3.resource('s3')
    bucket = s3_resource.Bucket(bucket_name)

    print(f"Esvaziando bucket: {bucket_name}")
    # Deletar objetos normais
    try:
        bucket.objects.all().delete()
    except Exception as e:
        print(f"Erro ao deletar objetos: {e}")

    # Deletar objetos versionados
    try:
        bucket.object_versions.all().delete()
    except Exception as e:
        print(f"Erro ao deletar versões: {e}")

def main():
    response = s3.list_buckets()
    buckets = response.get('Buckets', [])

    if not buckets:
        print("Nenhum bucket encontrado.")
        return

    for bucket in buckets:
        name = bucket['Name']
        if name.startswith("crossplane"):
            try:
                empty_bucket(name)
                print(f"Bucket {name} esvaziado com sucesso.")
            except Exception as e:
                print(f"Erro ao processar o bucket {name}: {e}")

if __name__ == "__main__":
    main()
