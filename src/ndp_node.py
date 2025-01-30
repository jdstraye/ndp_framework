'''
Class to represent a node with NDP.
'''
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Union
from microcontroller import Microcontroller


@dataclass
class NDP_Node:
    
    id: str
    storage_node: Union[str, Path]
    dsp: Microcontroller

    def __post_init__(self):
        with open(self.storage_node, 'r') as file:
            self.dsp.memory = file.readlines()[:int(len(self.dsp.memory))]  # Load code into memory (truncated to 256 lines)

    @property
    def id(self) -> str:
        return self._id

    @id.setter
    def id(self, id: str) -> None:
        self._id = id

    @property
    def storage_node(self) -> Union[str, Path]:
        return self._storage_node

    @storage_node.setter
    def storage_node(self, storage_node: Union[str, Path]) -> None:
        self._storage_node = storage_node

    @property
    def dsp(self) -> Microcontroller:
        return self._dsp

    @dsp.setter
    def dsp(self, dsp: Microcontroller) -> None:
        self._dsp = dsp
        
    def execute_node_code(self):
        try:
            code = "\n".join(self.dsp.memory)  # Combine lines of code
            
            logging.debug(f"Before formatting:\n{code}")
            
            # Replace variables with the node's actual values
            local_context = {"node_id": self.id, "storage_node": self.storage_node, "result": None}  # Context for exec()

            formatted_code = code.format(
                node=self,
                storage_node=self.storage_node.as_posix()
            )
            logging.debug(f"After formatting:\n{formatted_code}")
            
            exec(formatted_code, {}, local_context)  # Run code in isolated context
            logging.info(f"Node {self.id} executed code with result: {local_context.get('result')}")
        except Exception as e:
            logging.error(f"Node {self.id} failed to execute code: {e}")
