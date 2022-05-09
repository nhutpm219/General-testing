### Expected output:
#{
#  "app_name" = "crm_api"
#  "ip_address" = "127.0.0.1"
#}

locals {
  params = [
    {key = "app_name", value = "crm_api"},
    {key = "ip_address", value = "127.0.0.1"}
  ]

  params_dict = { for x in local.params : x.key => x.value }
}
