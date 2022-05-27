input("This is test:")
input("This is test:")
input("This is test:")

<nav className="d-flex justify-content-center">
    <ul className="pagination">
        {
        pages.map((page) => (
            <li className={page === currentPage ? "page-item active" : "page-item "}>
            <p className="page-link"
                onClick={() => pagination(page)}
            >{page}</p>
            </li>
        ))
        }
    </ul>
</nav>