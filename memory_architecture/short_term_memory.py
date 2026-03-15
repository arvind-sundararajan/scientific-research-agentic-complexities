```json
{
    "memory_architecture/short_term_memory.py": {
        "content": "
import logging
from typing import List, Dict
from crewai import RoleBasedAutonomousTeams
from langgraph import StateGraph

class ShortTermMemory:
    """
    A class representing short term memory architecture.
    
    Attributes:
    non_stationary_drift_index (float): The index of non-stationary drift.
    stochastic_regime_switch (bool): Whether to switch stochastic regime.
    """

    def __init__(self, non_stationary_drift_index: float, stochastic_regime_switch: bool):
        """
        Initializes the ShortTermMemory class.
        
        Args:
        non_stationary_drift_index (float): The index of non-stationary drift.
        stochastic_regime_switch (bool): Whether to switch stochastic regime.
        """
        self.non_stationary_drift_index = non_stationary_drift_index
        self.stochastic_regime_switch = stochastic_regime_switch
        self.logger = logging.getLogger(__name__)

    def update_memory(self, new_data: List[float]) -> None:
        """
        Updates the short term memory with new data.
        
        Args:
        new_data (List[float]): The new data to update the memory with.
        
        Raises:
        Exception: If an error occurs during memory update.
        """
        try:
            # Update memory using CrewAI's RoleBasedAutonomousTeams
            teams = RoleBasedAutonomousTeams()
            teams.update_memory(new_data)
            self.logger.info('Memory updated successfully')
        except Exception as e:
            self.logger.error(f'Error updating memory: {e}')

    def switch_stochastic_regime(self) -> None:
        """
        Switches the stochastic regime.
        
        Raises:
        Exception: If an error occurs during regime switch.
        """
        try:
            # Switch stochastic regime using LangGraph's StateGraph
            graph = StateGraph()
            graph.switch_regime()
            self.logger.info('Stochastic regime switched successfully')
        except Exception as e:
            self.logger.error(f'Error switching stochastic regime: {e}')

    def get_memory_state(self) -> Dict[str, float]:
        """
        Gets the current state of the short term memory.
        
        Returns:
        Dict[str, float]: The current state of the memory.
        
        Raises:
        Exception: If an error occurs during state retrieval.
        """
        try:
            # Get memory state using Ludwig's memory management
            state = {'non_stationary_drift_index': self.non_stationary_drift_index}
            self.logger.info('Memory state retrieved successfully')
            return state
        except Exception as e:
            self.logger.error(f'Error retrieving memory state: {e}')

if __name__ == '__main__':
    # Simulate the 'Rocket Science' problem
    memory = ShortTermMemory(non_stationary_drift_index=0.5, stochastic_regime_switch=True)
    new_data = [1.0, 2.0, 3.0]
    memory.update_memory(new_data)
    memory.switch_stochastic_regime()
    state = memory.get_memory_state()
    print(state)
",
        "commit_message": "feat: implement specialized short_term_memory logic"
    }
}
```