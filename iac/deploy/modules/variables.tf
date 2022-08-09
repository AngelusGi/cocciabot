## Variables

variable "resourcePrefix" {
  type        = string
  description = "Resource prefix name"
  default = "TelegramBot"
}

variable "azureRegion" {
  type        = string
  default     = "westeurope"
  description = "Default Azure Region"
}

