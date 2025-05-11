provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  token                  = data.aws_eks_cluster_auth.cluster.token
}

data "aws_eks_cluster_auth" "cluster" {
  name = module.eks.cluster_name
}


resource "kubernetes_deployment" "app" {
  metadata {
    name   = var.app_name
    labels = { app = var.app_name }
  }
  spec {
    replicas = 1
    selector { match_labels = { app = var.app_name } }
    template {
      metadata { labels = { app = var.app_name } }
      spec {
        container {
          name  = var.app_name
          image = "${aws_ecr_repository.app.repository_url}:latest"
          port { container_port = 8080 }
          resources {
            requests = { cpu = "250m", memory = "512Mi" }
            limits   = { cpu = "500m", memory = "1Gi" }
          }
        }
        # Uncomment for GPU jobs:
        # node_selector = { "role" = "gpu" }
        # tolerations = [{ key = "nvidia.com/gpu", operator = "Exists", effect = "NoSchedule" }]
      }
    }
  }
}

resource "kubernetes_service" "app" {
  metadata { name = var.app_name }
  spec {
    selector = { app = var.app_name }
    port {
      port        = 8080
      target_port = 8080
    }
    type = "LoadBalancer"
  }
}