import asyncio
import random
from enum import Enum, auto


class Action(Enum):
    HIGHKICK = auto()
    LOWKICK = auto()
    HIGHBLOCK = auto()
    LOWBLOCK = auto()


class Agent:
    def __init__(self, health=5):
        self.health = health
        self.actions = list(Action)

    async def __aiter__(self):
        return self

    async def __anext__(self):
        agent_move = random.choice(self.actions)
        neo_move = ""

        if agent_move is Action.LOWBLOCK:
            neo_move = Action.HIGHKICK
            self.health -= 1

        if agent_move is Action.LOWKICK:
            neo_move = Action.LOWBLOCK

        if agent_move is Action.HIGHBLOCK:
            neo_move = Action.LOWKICK
            self.health -= 1

        if agent_move is Action.HIGHKICK:
            neo_move = Action.HIGHBLOCK

        return neo_move, agent_move


async def fight():
    agent = Agent()
    while agent.health > 0:
        neo_move, agent_move = await agent.__anext__()
        print(f'Agent: {agent_move}, Neo: {neo_move}, Agent Health: {agent.health}')
    print('Neo wins!')


async def fightmany(n):
    agents = [Agent() for _ in range(n)]
    agents_numbers = [i for i in range(len(agents))]
    while [agent.health for agent in agents] != [0 for _ in agents_numbers]:
        agent_number = random.choice(agents_numbers)
        agent = agents[agent_number]
        if agent.health == 0:
            continue
        neo_move, agent_move = await agent.__anext__()
        print(
            f'Agent {agent_number + 1}: {agent_move}, Neo: {neo_move}, Agent {agent_number + 1} Health: {agent.health}')
    print('Neo wins!')

if __name__ == '__main__':
    asyncio.run(fight())
    asyncio.run(fightmany(3))
