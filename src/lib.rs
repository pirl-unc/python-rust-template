extern crate pyo3;
use pyo3::prelude::*;


#[pyfunction]
fn add_numbers(py: Python, a: i32, b: i32) -> Py<PyAny> {
    let summed_value: i32 = a + b;
    let my_string: String = summed_value.to_string();
    return Python::with_gil(|py| {
        my_string.to_object(py)
    });
}

#[pymodule]
fn testpkgrs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(add_numbers, m)?);
    Ok(())
}
