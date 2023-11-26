import objects
import serializers


movie1 = objects.Movie("1", "Twilight", "2008")
movie2 = objects.Movie("2", "The Hunger Games", "2012")
performance1 = objects.Performance("1", "Hamlet / Sociopath", "The old house")
performance2 = objects.Performance("2", "Cinderella", "Novosibirsk opera and ballet theatre")

os = serializers.ObjectSerializer()
print(os.serialize(movie1, 'JSON'))
print(os.serialize(movie2, 'XML'))
print(os.serialize(performance1, 'JSON'))
print(os.serialize(performance2, 'default'))