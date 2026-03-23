from langchain_core.messages import HumanMessage
from agent import build_agent


def main():
    agent = build_agent()

    print('Agent ready! Type quit to exit.')
    history = []

    while True:
        user_input = input('\nYou: ').strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            break

        if not user_input:
            continue

        history.append(HumanMessage(content=user_input))

        try:
            result = agent.invoke(
                {'messages': history},
                config={'recursion_limit': 30}
            )
            final = result['messages'][-1]
            print(f'\nAgent: {final.content}')
            history.append(final)

        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()