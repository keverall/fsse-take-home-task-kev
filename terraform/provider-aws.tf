terraform {
  # specify minimum version of Terraform
  required_version = ">= 1.4.0"
  required_providers {
    aws = { source = "hashicorp/aws"
    version = "~> 5.0" }
    kubernetes = { source = "hashicorp/kubernetes", version = "~> 2.1.0" }
    null = {
      source  = "hashicorp/null"
      version = "~> 3.1.0"
    }
    external = {
      source  = "hashicorp/external"
      version = "~> 2.1.0"
    }
    helm = {
      source  = "hashicorp/helm"
      version = "~> 2.4.1"
    }
    local = {
      source  = "hashicorp/local"
      version = "~> 2.1.0"
    }
  }
}

provider "aws" {
  region                   = var.aws_region
  profile                  = var.profile
  shared_credentials_files = ["~/.aws/credentials"]
}

