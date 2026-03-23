from langchain_core.messages import HumanMessage
from agent import build_agent
from token_tracker import TokenTracker


def main():
    agent = build_agent()
    tracker = TokenTracker(model='llama-3.1-8b-instant')

    print('Agent ready! Type quit to exit.')
    history = []

    while True:
        user_input = input('\nYou: ').strip()

        if user_input.lower() in ['quit', 'exit', 'q']:
            print(tracker.summary())
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

            if hasattr(final, 'usage_metadata') and final.usage_metadata:
                tracker.record(final.usage_metadata)

            print(f'\nAgent: {final.content}')
            history.append(final)

        except Exception as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    main()