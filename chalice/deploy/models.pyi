from typing import List, Dict, Any, TypeVar, Union, Optional
import enum

class Placeholder(enum.Enum):
    BUILD_STAGE = 'build_stage'
    DEPLOY_STAGE = 'deploy_stage'


class Instruction:
    pass


class APICall(Instruction):
    method_name = ...  # type: str
    params = ...  # type: Dict[str, Any]
    resource = ...  # type: Optional[ManagedModel]

    def __init__(self,
                 method_name,           # type: str
                 params,                # type: Dict[str, Any]
                 resource=None,         # type: Optional[ManagedModel]
                 ):
        # type: (...) -> None
        ...

class StoreValue(Instruction):
    name = ...  # type: str

    def __init__(self,
                 name,  # type: str
                 ):
        # type: (...) -> None
        ...

class RecordResourceValue(Instruction):
    resource_type = ...  # type: str
    resource_name = ...  # type: str
    name = ...  # type: str
    variable_name = ...  # type: Any

    def __init__(self,
                 resource_type,       # type: str
                 resource_name,       # type: str
                 name,                # type: str
                 variable_name=None,  # type: Any
                 ):
        # type: (...) -> None
        ...


class Push(Instruction):
    value = ...  # type: Any

    def __init__(self, value: Any) -> None: ...


class Pop(Instruction):
    pass


class JPSearch(Instruction):
    expression = ...  # type: str

    def __init__(self, expression: str) -> None: ...


T = TypeVar('T')
DV = Union[Placeholder, T]
STR_MAP = Dict[str, str]


class Model:
    def dependencies(self) -> List[Model]: ...


class ManagedModel(Model):
    resource_name = ...  # type: str
    resource_type = ...  # type: str


class Application(Model):
    stage = ...  # type: str
    resources = ... # type: List[Model]

    def __init__(self,
                 stage,       # type: str
                 resources,   # type: List[Model]
                 ):
        # type: (...) -> None
        ...


class DeploymentPackage(Model):
    filename = ...  # type: str

    def __init__(self,
                 filename,   # type: DV[str]
                 ):
        # type: (...) -> None
        ...


class IAMPolicy(Model):
    pass


class FileBasedIAMPolicy(IAMPolicy):
    filename = ...  # type: str

    def __init__(self,
                 filename,   # type: str
                 ):
        # type: (...) -> None
        ...


class AutoGenIAMPolicy(IAMPolicy):
    document = ...  # type: DV[Dict[str, Any]]

    def __init__(self,
                 document,   # type: DV[Dict[str, Any]]
                 ):
        # type: (...) -> None
        ...


class IAMRole(Model):
    role_arn = ... # type: DV[str]


class PreCreatedIAMRole(IAMRole):
    role_arn = ... # type: str

    def __init__(self,
                 role_arn,   # type: str
                 ):
        # type: (...) -> None
        ...


class ManagedIAMRole(IAMRole, ManagedModel):
    role_arn = ... # type: DV[str]
    role_name = ... # type: str
    trust_policy = ... # type: Dict[str, Any]
    policy = ... # type: IAMPolicy

    def __init__(self,
                 resource_name,  # type: str
                 role_arn,       # type: DV[str]
                 role_name,      # type: str
                 trust_policy,   # type: Dict[str, Any]
                 policy,         # type: IAMPolicy
                 ):
        # type: (...) -> None
        ...


class LambdaFunction(ManagedModel):
    function_name = ... # type: str
    deployment_package = ... # type: DeploymentPackage
    environment_variables = ... # type: STR_MAP
    runtime = ... # type: str
    handler = ... # type: str
    tags = ... # type: STR_MAP
    timeout = ... # type: int
    memory_size = ... # type: int
    role = ... # type: IAMRole

    def __init__(self,
                 resource_name,           # type: str
                 function_name,           # type: str
                 deployment_package,      # type: DeploymentPackage
                 environment_variables,   # type: STR_MAP
                 runtime,                 # type: str
                 handler,                 # type: str
                 tags,                    # type: STR_MAP
                 timeout,                 # type: int
                 memory_size,             # type: int
                 role,                    # type: IAMRole
                 ):
        # type: (...) -> None
        ...