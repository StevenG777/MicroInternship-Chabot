import itertools

## Generate more data for modeling
# Define the options for each part of the sentence
verbs = ["aspire", "want"]
wondering = ["am wondering what to", "am wondering what I can"]
become = ["be a", "become a", "work as a"]
work = ["work with", "be working in", "work in"]
about = [" about", ""]
actions = ["improve", "enhance", "learn", "advance", "boost", "hone", "increase", "gain", "develop"]
take = ["take", "register for", "be recommended to take"]
my = [" my", ""]
job_titles = ["software engineer", "software developer", "mobile app developer", "web developer"]
subjects = ["software engineering", "software development", "mobile development", "web development"]
the = [" the", ""]
industry = ["industry", "field"]

web_keywords = ["web", "web industry", "web developer", "web developer", "web courses"]
software_keywords = ["software", "software major", "software devloper", "software engineer", "software courses", "software industry"]
data_keywords = ["data", "data science", "data engineering", "computer vision", "data major", "data scientist"]

# # Generate all possible combinations
# combinations = list(itertools.product(wondering, take, subjects))
# # Print out the combinations
# for combo in combinations:
#     print(f"\"I {combo[0]} {combo[1]} {combo[2]} courses\",")

with open('temp.txt', 'w') as f:
    # Generate all possible permutations
    arr = data_keywords
    for r in range(1, len(arr) + 1):
        combinations = itertools.combinations(arr, r)
        for comb in combinations:
            permutations = list(itertools.permutations(comb))
            # Print out the permutation
            for per in permutations:
                f.write("\"" + " ".join(per) + "\",\n")
                print("\"" + " ".join(per) + "\",\n")