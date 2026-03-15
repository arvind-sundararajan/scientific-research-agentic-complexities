```json
{
    "utils/evaluation_metrics.py": {
        "content": "
import logging
from typing import Dict, List
from crewai import RoleBasedAutonomousTeams
from langgraph import StateGraph

logging.basicConfig(level=logging.INFO)

def calculate_non_stationary_drift_index(data: List[float]) -> float:
    """
    Calculate the non-stationary drift index for a given dataset.

    Args:
    - data (List[float]): The input dataset.

    Returns:
    - float: The non-stationary drift index.
    """
    try:
        # Calculate the mean and standard deviation of the data
        mean = sum(data) / len(data)
        std_dev = (sum((x - mean) ** 2 for x in data) / len(data)) ** 0.5
        
        # Calculate the non-stationary drift index
        non_stationary_drift_index = (std_dev / mean) * 100
        
        logging.info('Non-stationary drift index calculated successfully.')
        return non_stationary_drift_index
    
    except ZeroDivisionError:
        logging.error('Error: Division by zero occurred while calculating non-stationary drift index.')
        return None

def evaluate_stochastic_regime_switch(model: RoleBasedAutonomousTeams, data: List[float]) -> Dict[str, float]:
    """
    Evaluate the stochastic regime switch for a given model and dataset.

    Args:
    - model (RoleBasedAutonomousTeams): The input model.
    - data (List[float]): The input dataset.

    Returns:
    - Dict[str, float]: A dictionary containing the evaluation metrics.
    """
    try:
        # Initialize the evaluation metrics dictionary
        evaluation_metrics = {}
        
        # Calculate the non-stationary drift index
        non_stationary_drift_index = calculate_non_stationary_drift_index(data)
        
        # Calculate the stochastic regime switch metrics
        state_graph = model.get_state_graph()
        stochastic_regime_switch_metrics = state_graph.evaluate_regime_switch(data)
        
        # Update the evaluation metrics dictionary
        evaluation_metrics['non_stationary_drift_index'] = non_stationary_drift_index
        evaluation_metrics['stochastic_regime_switch_metrics'] = stochastic_regime_switch_metrics
        
        logging.info('Stochastic regime switch evaluated successfully.')
        return evaluation_metrics
    
    except Exception as e:
        logging.error(f'Error: {str(e)} occurred while evaluating stochastic regime switch.')
        return None

def simulate_rocket_science_problem() -> None:
    """
    Simulate the 'Rocket Science' problem using the CrewAI and LangGraph libraries.
    """
    try:
        # Initialize the CrewAI model
        model = RoleBasedAutonomousTeams()
        
        # Initialize the LangGraph state graph
        state_graph = StateGraph()
        
        # Simulate the rocket science problem
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        evaluation_metrics = evaluate_stochastic_regime_switch(model, data)
        
        # Print the evaluation metrics
        print(evaluation_metrics)
        
        logging.info('Rocket science problem simulated successfully.')
    
    except Exception as e:
        logging.error(f'Error: {str(e)} occurred while simulating rocket science problem.')

if __name__ == '__main__':
    simulate_rocket_science_problem()
",
        "commit_message": "feat: implement specialized evaluation_metrics logic"
    }
}
```