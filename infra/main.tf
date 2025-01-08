module "resource_group" {
  source = "github.com/AngelusGi/azure_terraform.git//modules/resource_group?ref=develop"

  location = var.location
  name     = var.rg_name

}

module "key_vault" {
  source = "github.com/AngelusGi/azure_terraform.git//modules/key_vault?ref=develop"
  # source = "github.com/AngelusGi/azure_terraform.git//modules/key_vault?ref=0.0.2"

  resource_group_name = module.resource_group.name
  location            = module.resource_group.location
  name                = var.keyvault_name
  tags                = module.resource_group.tags

  depends_on = [module.resource_group]
}
