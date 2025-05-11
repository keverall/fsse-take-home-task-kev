# FastAPI Asynchronous Pair Programming Task

## Overview  

Your task will be to build a FastAPI-based web service that interacts asynchronously with a simulated neural network 
backend. The service will receive requests from many clients, batch different parts of the requests together and relay 
those batches onto the backend. The service should efficiently handle multiple client requests while ensuring proper 
deployment practices.

This is a skeleton repo for you to start with which has the Pydantic models used by the clients to send data in their 
requests as well as scripts for sending a client request with the requests library and with locust. You also have 
Pydantic models that we will assume the backend neural networks send back to your service.

## Requirements  

1. Implement a FastAPI web app with a POST /predict endpoint that receives a JSON payload (Pydantic model for this 
payload is given), batches the data together and relays it to the backend.
2. The FastAPI web app will not need to perform or send actual requests to a neural network backend, instead it will be 
mocked. We’ll assume the request takes 3-7 seconds to process on the neural network backend. 
3. Each request may use multiple different neural networks so you’ll need a way to split the client requests between 
the different neural networks, batch them with other requests to the same network, and then to disseminate the 
results back to the corresponding client. 
4. The code should be structured, modular and follow best practices.

## Details  

The client will send a JSONified Pydantic model which includes a dictionary mapping strings to “agent” requests. Each 
agent request will have at least a vector (list[float]), model name (str) and agent type (str) within it.

Your service should take each agent request, split them and then batch them with other agent requests that have the same
 agent type and that requested the same model as one another. You should end up with a JSON payload to send to the 
backend which houses a list of vectors (list[list[float]] - a matrix) and will receive a response with a vector 
(list[float]) from the backend.

The response from the backend will need to be split up and distributed back to the corresponding clients who made up 
that particular batch of agent requests.

## Installation  

Ensure that python3.12, python3.12 venv, and make is installed:

### Ubuntu / Debian  

```commandline
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt update
sudo apt install python3.12 python3.12-venv make
```

### MacOS with brew  

```commandline
brew install python@3.12
brew install make
```

### Create Virtual Environment & Install Package

```commandline
make venv
make install
```

### Terraform Docs - Generated  

```commandline
cd terraform
terraform-docs markdown table --output-file ../README.md --output-mode inject .
```

<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | >= 1.4.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 5.0 |
| <a name="requirement_external"></a> [external](#requirement\_external) | ~> 2.1.0 |
| <a name="requirement_helm"></a> [helm](#requirement\_helm) | ~> 2.4.1 |
| <a name="requirement_kubernetes"></a> [kubernetes](#requirement\_kubernetes) | ~> 2.1.0 |
| <a name="requirement_local"></a> [local](#requirement\_local) | ~> 2.1.0 |
| <a name="requirement_null"></a> [null](#requirement\_null) | ~> 3.1.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | 5.97.0 |
| <a name="provider_kubernetes"></a> [kubernetes](#provider\_kubernetes) | 2.1.0 |

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_eks"></a> [eks](#module\_eks) | terraform-aws-modules/eks/aws | n/a |

## Resources

| Name | Type |
|------|------|
| [aws_eks_identity_provider_config.oidc](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/eks_identity_provider_config) | resource |
| [kubernetes_deployment.app](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/deployment) | resource |
| [kubernetes_service.app](https://registry.terraform.io/providers/hashicorp/kubernetes/latest/docs/resources/service) | resource |
| [aws_availability_zones.az](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/availability_zones) | data source |
| [aws_caller_identity.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/caller_identity) | data source |
| [aws_eks_cluster_auth.cluster](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/eks_cluster_auth) | data source |
| [aws_kms_alias.s3](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/kms_alias) | data source |
| [aws_region.current](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/data-sources/region) | data source |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_app_name"></a> [app\_name](#input\_app\_name) | n/a | `string` | `"fsse-app"` | no |
| <a name="input_aws_region"></a> [aws\_region](#input\_aws\_region) | n/a | `string` | `"us-west-2"` | no |
| <a name="input_ecr_repo_name"></a> [ecr\_repo\_name](#input\_ecr\_repo\_name) | ECR repository name | `string` | `"fsse-app-repo"` | no |
| <a name="input_eks_cluster_name"></a> [eks\_cluster\_name](#input\_eks\_cluster\_name) | n/a | `string` | `"fsse-eks-cluster"` | no |
| <a name="input_env"></a> [env](#input\_env) | Environment name | `string` | `"dev"` | no |
| <a name="input_github_repo_name"></a> [github\_repo\_name](#input\_github\_repo\_name) | GitHub repository name | `string` | `"fsse-app"` | no |
| <a name="input_profile"></a> [profile](#input\_profile) | The name of the AWS profile in the credentials file | `string` | `"default"` | no |
| <a name="input_public_subnets"></a> [public\_subnets](#input\_public\_subnets) | n/a | `list(string)` | n/a | yes |
| <a name="input_vpc_id"></a> [vpc\_id](#input\_vpc\_id) | n/a | `any` | n/a | yes |

## Outputs

| Name | Description |
|------|-------------|
| <a name="output_ecr_repo_url"></a> [ecr\_repo\_url](#output\_ecr\_repo\_url) | n/a |
| <a name="output_eks_cluster_name"></a> [eks\_cluster\_name](#output\_eks\_cluster\_name) | n/a |
| <a name="output_service_url"></a> [service\_url](#output\_service\_url) | n/a |
<!-- END_TF_DOCS -->