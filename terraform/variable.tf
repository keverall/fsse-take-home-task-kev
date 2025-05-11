variable "aws_region" { default = "us-west-2" }
variable "app_name" { default = "fsse-app" }
variable "eks_cluster_name" { default = "fsse-eks-cluster" }
variable "vpc_id" {}
variable "public_subnets" { type = list(string) }

variable "env" {
  description = "Environment name"
  type        = string
  default     = "dev"
}

variable "github_repo_name" {
  description = "GitHub repository name"
  type        = string
  default     = "fsse-app"
}

variable "ecr_repo_name" {
  description = "ECR repository name"
  type        = string
  default     = "fsse-app-repo"
}


variable "profile" {
  description = "The name of the AWS profile in the credentials file"
  type        = string
  default     = "default"
}


