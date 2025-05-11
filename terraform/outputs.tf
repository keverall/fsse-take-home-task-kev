output "ecr_repo_url" { value = aws_ecr_repository.app.repository_url }
output "eks_cluster_name" { value = module.eks.cluster_name }
output "service_url" { value = kubernetes_service.app.status[0].load_balancer.ingress[0].hostname }