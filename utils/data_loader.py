```json
{
    "utils/data_loader.py": {
        "content": "
import logging
from typing import Dict, List
from crewai import RoleBasedAutonomousTeams
from langgraph import StateGraph

def load_non_stationary_data(non_stationary_drift_index: int, stochastic_regime_switch: bool) -> Dict:
    """
    Load non-stationary data based on the provided drift index and regime switch.

    Args:
    - non_stationary_drift_index (int): The index of the non-stationary drift.
    - stochastic_regime_switch (bool): Whether to apply stochastic regime switch.

    Returns:
    - Dict: A dictionary containing the loaded non-stationary data.
    """
    try:
        logging.info('Loading non-stationary data...')
        data = RoleBasedAutonomousTeams.load_data(non_stationary_drift_index, stochastic_regime_switch)
        logging.info('Non-stationary data loaded successfully.')
        return data
    except Exception as e:
        logging.error(f'Error loading non-stationary data: {e}')
        return {}

def load_state_graph(state_graph_id: str) -> StateGraph:
    """
    Load a state graph based on the provided ID.

    Args:
    - state_graph_id (str): The ID of the state graph.

    Returns:
    - StateGraph: The loaded state graph.
    """
    try:
        logging.info(f'Loading state graph {state_graph_id}...')
        state_graph = StateGraph.load_state_graph(state_graph_id)
        logging.info(f'State graph {state_graph_id} loaded successfully.')
        return state_graph
    except Exception as e:
        logging.error(f'Error loading state graph {state_graph_id}: {e}')
        return None

def simulate_rocket_science(state_graph: StateGraph, non_stationary_data: Dict) -> List:
    """
    Simulate the 'Rocket Science' problem using the provided state graph and non-stationary data.

    Args:
    - state_graph (StateGraph): The state graph to use for simulation.
    - non_stationary_data (Dict): The non-stationary data to use for simulation.

    Returns:
    - List: A list of simulation results.
    """
    try:
        logging.info('Simulating Rocket Science problem...')
        simulation_results = state_graph.simulate(non_stationary_data)
        logging.info('Rocket Science problem simulation completed.')
        return simulation_results
    except Exception as e:
        logging.error(f'Error simulating Rocket Science problem: {e}')
        return []

if __name__ == '__main__':
    non_stationary_drift_index = 1
    stochastic_regime_switch = True
    state_graph_id = 'rocket_science_state_graph'

    non_stationary_data = load_non_stationary_data(non_stationary_drift_index, stochastic_regime_switch)
    state_graph = load_state_graph(state_graph_id)
    simulation_results = simulate_rocket_science(state_graph, non_stationary_data)

    print('Simulation Results:')
    print(simulation_results)
",
        "commit_message": "feat: implement specialized data_loader logic"
    }
}
```