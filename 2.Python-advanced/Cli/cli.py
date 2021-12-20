from python_click import current_weather
import click

@click.command()
@click.argument('location')
def main(location):
    print("I'm a beautiful CLI ✨")
    weather = current_weather(location)
    print(f"The weather in {location} right now: {weather}.")

if __name__ == "__main__":
    main()




