# module "eks" {
#   source          = "terraform-aws-modules/eks/aws"
#   cluster_name    = var.eks_cluster_name
#   cluster_version = "1.29"
#   vpc_id          = var.vpc_id
#   subnet_ids      = var.public_subnets

#   eks_managed_node_groups = {
#     cost_optimized = {
#       desired_size   = 1
#       max_size       = 2
#       min_size       = 1
#       instance_types = ["t3.medium"]
#       capacity_type  = "SPOT"
#       labels         = { role = "app" }
#     }
#     gpu = {
#       desired_size   = 0
#       max_size       = 2
#       min_size       = 0
#       instance_types = ["g4dn.xlarge"] # NVIDIA T4 GPU, good for AI/ML
#       capacity_type  = "ON_DEMAND"
#       labels         = { role = "gpu" }
#       taints         = [{ key = "nvidia.com/gpu", value = "present", effect = "NO_SCHEDULE" }]
#     }
#   }
#   tags = {
#     Name             = var.eks_cluster_name
#     Environment      = var.env
#     Repo             = var.github_repo_name
#     ecr_repo_nameame = var.ecr_repo_name
#     AppName          = var.app_name

#   }
# }