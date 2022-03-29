# polarsbear

Superset Python package for [Polars](https://github.com/pola-rs/polars).

## Goals

`polarsbear` tries to implement the good and trim the bad from the `pandas` API but as an implementation on top of `polars`.

`polars` intends to provide better performanace, but also aims to implement a higher quality `DataFrame` API. A tradeoff from doing this is the potential to alienate certain `pandas` users.

`pandas` has an API that is sometimes inconsistent. One example would be that certain methods are designed for multiple different input data types.

One major reason to use `polars` over `pandas` is for the performance gain. Another reason could be its memory philosophy. Unfortunately this produces tradeoffs that might bloat `polars` onboarding in a way that specific `pandas` users won't find worth it.

**In summary, `polarsbears` *adds* to `polars` what `polars` does not implement for design continuity or other good reasons.**
