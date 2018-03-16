extern crate clap;
extern crate rand;

use rand::Rng;
use clap::{App, Arg};

fn main() {
    let matches = App::new("rgg")
        .version("0.0.0")
        .author("Jeremy Day <jadaytime@gmail.com>")
        .about("rust graph generator - generates random graphs with the intention of being input for code-a-thon problems")
        .arg(
            Arg::with_name("number_of_nodes")
                .short("n")
                .long("number-of-nodes")
                .help("The number of nodes in the resulting graph.")
                .required(true)
                .value_name("INTEGER"),
        )
        .arg(
            Arg::with_name("edge_chance")
                .short("c")
                .long("edge-chance")
                .help("The percentage chance that two nodes will have an edge between them.")
                .required(true)
                .value_name("FLOAT"),
        )
        .get_matches();

    let num_nodes: usize = matches
        .value_of("number_of_nodes")
        .unwrap()
        .parse()
        .unwrap();
    let edge_chance: f32 = matches.value_of("edge_chance").unwrap().parse().unwrap();
    let mut rng = rand::thread_rng();
    print_adjacency_list(&construct_adjacency_list(
        num_nodes,
        0..num_nodes,
        edge_chance,
        rng.gen_iter::<u32>(),
    ));
}

fn print_adjacency_list<T, U>(adjacentcy_list: &[(T, Vec<(T, U)>)])
where
    T: std::fmt::Display,
    U: std::fmt::Display,
{
    for node in adjacentcy_list {
        let mut line = String::new();
        let num_edges = node.1.len();
        line.push_str(&format!("{} {}", &node.0, num_edges));
        for &(ref label, ref weight) in &node.1 {
            line.push_str(&format!(" {} {}", label, weight));
        }
        println!("{}", &line);
    }
}

fn construct_adjacency_list<T, I, J>(
    num_nodes: usize,
    mut labels: I,
    edge_chance: f32,
    mut weights: J,
) -> Vec<(T, Vec<(T, u32)>)>
where
    I: Iterator<Item = T>,
    J: Iterator<Item = u32>,
    T: std::clone::Clone,
{
    let mut nodes: Vec<(T, Vec<(T, u32)>)> = Vec::with_capacity(num_nodes);
    for i in 0..num_nodes {
        match labels.next() {
            Some(x) => nodes.push((x, Vec::<(T, u32)>::new())),
            None => panic!("Lables iterator did not produce enough labels. Needed {} labels to account for all nodes, iterator produced only {}.", num_nodes, i),
        }
    }
    for i in 0..num_nodes {
        for j in i + 1..num_nodes {
            let rand = rand::random::<f32>();
            if rand <= edge_chance {
                match weights.next() {
                    Some(x) => {
                        let label = nodes[j].0.clone();
                        nodes[i].1.push((label, x + 100));
                    },
                    None => panic!("Weights iterator did not produce enough weights. You should use an infinite iterator, or one with at least {}^2 ({}) to potentially construct a complete graph.", num_nodes, num_nodes * num_nodes),
                }
            }
        }
    }
    nodes
}
