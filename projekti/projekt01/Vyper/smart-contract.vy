
#pip install vyper
struct Entry:
    id: int128
    username: String[100]
    github_link: String[200]
    filename: String[100]

entries: HashMap[int128, Entry]

entry_count: public(int128)

# Function to add a new entry
@external
def add_entry(_username: String[100], _github_link: String[200], _filename: String[100]):
    assert len(_username) != 0
    assert len(_github_link) != 0
    assert len(_filename) != 0
    self.entries[self.entry_count] = Entry({id: self.entry_count, username: _username, github_link: _github_link, filename : _filename})
    self.entry_count += 1
# Function to retrieve an entry by its ID
@external
def get_entry(entry_id: int128) -> Entry:
    return self.entries[entry_id]
