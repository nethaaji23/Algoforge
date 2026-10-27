from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field

class AuthRequest(BaseModel):
    email: str
    password: str
    username: Optional[str] = None

class OAuthRequest(BaseModel):
    provider: str
    email: Optional[str] = None
    username: Optional[str] = None

class AuthResponse(BaseModel):
    success: bool
    message: str
    user: Optional[Dict[str, Any]] = None
    token: Optional[str] = None

class AlgorithmRequest(BaseModel):
    algorithm: str = Field(..., example="bubble_sort")
    problem_id: Optional[str] = Field(default=None, example="P002")
    data: List[int] = Field(default_factory=lambda: [5, 2, 8, 3, 1, 9, 4, 6])
    target: Optional[int] = None
    speed: float = Field(default=1.0)

class Node3D(BaseModel):
    id: str
    label: str
    val: Any
    x: float
    y: float
    z: float
    color: str = "#f97316"  # Cyber Lime
    status: str = "idle"
    scale: float = 1.0
    layer: int = 0

class Edge3D(BaseModel):
    source: str
    target: str
    color: str = "#444933"
    label: Optional[str] = None

class StackFrame(BaseModel):
    func_name: str
    line_no: int
    args: Dict[str, Any]

class VariableState(BaseModel):
    name: str
    type_str: str
    value: str
    is_changed: bool = False

class ExecutionStep(BaseModel):
    step_index: int
    line_number: int
    description: str
    call_stack: List[StackFrame]
    variables: List[VariableState]
    nodes: List[Node3D]
    edges: List[Edge3D]
    active_node_ids: List[str] = Field(default_factory=list)

class ExecutionResponse(BaseModel):
    algorithm: str
    title: str
    total_steps: int
    steps: List[ExecutionStep]
