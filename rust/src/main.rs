use std::{char, collections::HashMap};
use tracing::info;

fn main() {
    tracing_subscriber::fmt::init();
}
fn are_parenthesis_valid(text: &str) -> bool {
    _are_parenthesis_valid("", text.split("").collect());
    return false;
}

fn _are_parenthesis_valid(before: &str, string: Vec<&str>) -> bool {
    let open_close_pairs = HashMap::from([("(", ")"), ("{", "}"), ("[", "]")]);
    if open_close_pairs.contains_key(string[0]) {
        return _are_parenthesis_valid(before, string);
    }
    return false;
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::HashMap;

    #[test]
    fn test() {
        tracing_subscriber::fmt::init();
        let test_cases = HashMap::from([
("(", false),
("()", true),
("([)", false),
(")", false),
("())", false),
("([{}])()[]{}", true),
("({[(())]})()", true),
("({[(())]})())", false),
("(((()", false),
("(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((())((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()", false),
("sdfasdf", false),
("(asdf)", false),
    ]
    );
        for (testStr, expectation) in test_cases.into_iter() {
            info!("request made");
            assert_eq!(are_parenthesis_valid(testStr), expectation);
        }
    }
}
