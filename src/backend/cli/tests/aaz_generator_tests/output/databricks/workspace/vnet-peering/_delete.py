# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long
# pylint: disable=too-many-lines

from azure.cli.core.aaz import *


@register_command(
    "databricks workspace vnet-peering delete",
    is_preview=True,
)
class Delete(AAZCommand):
    """Delete the vnet peering.

    :example: Delete the vnet peering.
        az databricks workspace vnet-peering delete --resource-group MyResourceGroup --workspace-name MyWorkspace -n MyPeering
    """

    _aaz_info = {
        "version": "2018-04-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.databricks/workspaces/{}/virtualnetworkpeerings/{}", "2018-04-01"],
        ]
    }

    AZ_SUPPORT_NO_WAIT = True

    def _handler(self, command_args):
        super()._handler(command_args)
        return self.build_lro_poller(self._execute_operations(), result_callback=None)

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.peering_name = AAZStrArg(
            options=["--peering-name", "--name", "-n"],
            help="The name of the workspace vNet peering.",
            required=True,
            id_part="child_name_1",
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )
        _args_schema.workspace_name = AAZStrArg(
            options=["--workspace-name"],
            help="The name of the workspace.",
            required=True,
            id_part="name",
        )
        return _args_schema

    def _execute_operations(self):
        yield self.VNetPeeringDelete(ctx=self.ctx)()

    class VNetPeeringDelete(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"
        ERROR_FORMAT = "ODataV4Format"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [202]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    deserialization_callback=self.on_200_202_204,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )
            if session.http_response.status_code in [200, 202, 204]:
                return self.client.build_lro_polling(
                    self.ctx.args.no_wait,
                    session,
                    deserialization_callback=self.on_200_202_204,
                    lro_options={"final-state-via": "azure-async-operation"},
                    path_format_arguments=self.url_parameters,
                )

            return self.on_error(session)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Databricks/workspaces/{workspaceName}/virtualNetworkPeerings/{peeringName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "DELETE"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "peeringName", self.ctx.args.peering_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
                **self.serialize_url_param(
                    "workspaceName", self.ctx.args.workspace_name,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2018-04-01",
                    required=True,
                ),
            }
            return parameters

        def on_200_202_204(self, session):
            pass


__all__ = ["Delete"]