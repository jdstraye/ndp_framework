from datetime import datetime
from logging.handlers import RotatingFileHandler
from microcontroller import Microcontroller
from ndp_node import NDP_Node
from pathlib import Path
from rich import print
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table
from typing import List, Tuple
import logging
import os

#from utils import Global

os.environ["PATH"] += ";C:\\Users\\jdstr\\AppData\\Roaming\\Python\\Python312\\Scripts"
#gv = Global()

def setup_logging(log_path=Path("logs/debug.log")):
    # Ensure the logs directory exists
    log_path.parent.mkdir(parents=True, exist_ok=True)
    # Create a rich handler for INFO and above
            
    try:
        rich_handler = RichHandler(
            level=logging.INFO, 
            console=Console(), 
            rich_tracebacks=True, 
            markup=True,
            show_time=False,  # Time will be handled by our formatter
            show_level=True   # Ensure level is shown
        )
        file_handler = RotatingFileHandler(
            "logs/debug.log", 
            maxBytes=10 * 2**20, 
            backupCount=5
        ) 
        file_handler.setLevel(logging.DEBUG)
        
        # Create a consistent formatter for both handlers
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        
        # Formatter for the Rich handler (leave rendering to Rich)
        rich_handler.setFormatter(formatter)

        # Remove any existing handlers to avoid duplication
        root = logging.getLogger()
        if root.handlers:
            for handler in root.handlers:
                root.removeHandler(handler)
                
        # Configure the root logger to capture everything (DEBUG and above)
        root.setLevel(logging.DEBUG)  # This ensures DEBUG messages are captured
        root.addHandler(file_handler)
        root.addHandler(rich_handler)
        
        logging.info(f"!!! Starting a new NDP Run -- {datetime.now().strftime("%Y-%m-%d %H:%M:%S")} !!!")
        logging.debug("Debug logging enabled for file output")  # Test message that should only appear in file

    except Exception as e:
        raise RuntimeError(f"Failed to set up logging: {e}")
        

def setup_nodes(configuration : Tuple[int,int], ndp_code = Path.cwd() / 'ndp_nodes' / 'ndp_code.asm', ndp_path = Path.cwd() / 'ndp_nodes' ) -> list[NDP_Node]:
    ndp_nodes = []
    for x in range(configuration[0]):
        for y in range(configuration[1]):
            dsp = Microcontroller(memory_size=1024, register_file_size=16)
            dsp.memory = ndp_code.read_text().splitlines()[:256] # Load code into memory (truncated to 256 lines)
            ndp_node = NDP_Node(id = (x,y), storage_node = ndp_code, dsp = dsp)
            ndp_nodes.append(ndp_node)
            logging.debug(f"Node '({x}, {y})' created")
    return ndp_nodes
    

def main(ndp_nodes: List[NDP_Node], ndp_path = Path.cwd() / 'ndp_nodes' ):
    logging.debug(f"{ndp_path.as_posix() = }")

    # Execute code for each node
    for node in ndp_nodes:
        node.execute_node_code()
        
if __name__ == "__main__":
    configuration = (5,5)
    setup_logging(log_path=Path("logs/debug.log"))
    ndp_dir = Path.cwd() / 'ndp_nodes'
    ndp_nodes = setup_nodes(configuration = configuration, ndp_code = ndp_dir / 'ndp_code.asm', ndp_path = ndp_dir)
    main(ndp_nodes=ndp_nodes, ndp_path=ndp_dir)



